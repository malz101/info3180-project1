"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from .forms import PropertyForm
from .models import Property

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Malz Housing")


@app.route('/property',methods=['GET', 'POST'])
def add_property():
    """displaying the form to add a new property"""
    property_form = PropertyForm()

    if request.method == 'POST':
        if property_form.validate_on_submit():
            # Note the difference when retrieving form data using Flask-WTF
            # Here we use myform.firstname.data instead of request.form['firstname']
            title = property_form.title.data
            description = property_form.description.data
            no_of_rooms = property_form.no_of_rooms.data
            no_of_bathrooms = property_form.no_of_bathrooms.data
            price = property_form.price.data
            type_ = property_form.type_.data
            location = property_form.location.data
            
            # Get file data and save to your uploads folder
            photo = property_form.photo.data

            filename = secure_filename(photo.filename)
            photo.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename
            ))

            # Add new property to database
            property_ = Property(title=title, description=description, no_of_rooms=no_of_rooms,\
                                    no_of_bathrooms=no_of_bathrooms, price=price, type_=type_,\
                                    location=location, photo=photo.filename)
            
            db.session.add(property_)
            db.session.commit()

            flash('You have successfully filled out the form', 'success')
            return redirect(url_for('properties'))

        flash_errors(property_form)
    return render_template('property_form.html', form=property_form)


@app.route('/properties')
def properties():
    """displaying a list of all properties in the database. """
    
    props = db.session.query(Property).order_by(Property.id).all()

    return render_template('properties.html',properties=props)

@app.route('/property/<propertyid>')
def property(propertyid):
    """For viewing an individual property by the specific property id"""
    prop = db.session.query(Property).filter(Property.id==propertyid).first()
    return render_template('property.html',prop=prop)


@app.route('/uploads/<filename>')
def get_image(filename):
    root_dir = os.getcwd()
    uploaddir = os.path.join(root_dir,app.config['UPLOAD_FOLDER'])
    return send_from_directory(uploaddir, filename)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
