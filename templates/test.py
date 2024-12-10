from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Flask-WTForms for the Welfare POD form
class PodForm(FlaskForm):
    site_location = StringField("Site Location", validators=[DataRequired()])
    pod_id = SelectField(
        "Welfare POD ID",
        choices=[("SRTB5102", "SRTB5102"), ("E71246", "E71246"),
                 ("E71264", "E71264"), ("E71275z", "E71275"), ("E71278", "E71278")]
    )
    pod_number = SelectField(
        "Welfare POD Number",
        choices=[("Pod1", "Pod1"), ("Pod2", "Pod2"), ("Pod3", "Pod3"),
                 ("Pod4", "Pod4"), ("Pod5", "Pod5")]
    )
    pod_usage = SelectField(
        "Pod Usage",
        choices=[("Sac Cabin", "Sac Cabin"), ("ES Cabin", "ES Cabin"),
                 ("Resource Canteen1", "Resource Canteen1"), 
                 ("Resource Canteen2", "Resource Canteen2"),
                 ("Resource Canteen3", "Resource Canteen3"),
                 ("Lavatory Facilities", "Lavatory Facilities")]
    )
    generator_status = SelectField(
        "Generator Status",
        choices=[("Functional", "Functional"), ("Non Functional", "Non Functional")]
    )
    cleaned_male = SelectField(
        "Cleaned Toilets Male",
        choices=[("Yes", "Yes"), ("No", "No")]
    )
    cleaned_female = SelectField(
        "Cleaned Toilets Female",
        choices=[("Yes", "Yes"), ("No", "No")]
    )
    diesel_gauge = IntegerField(
        "Diesel Gauge Status (%)", validators=[DataRequired(), NumberRange(min=0, max=100)]
    )
    oil_gauge = IntegerField(
        "Oil Gauge Status (%)", validators=[DataRequired(), NumberRange(min=0, max=100)]
    )
    storage = SelectField(
        "Used as Storage",
        choices=[("Yes", "Yes"), ("No", "No")]
    )
    comments = TextAreaField("Comments", validators=[Optional()])
    submit = SubmitField("Send Report")


@app.route("/", methods=["GET", "POST"])
def index():
    forms = [PodForm(prefix=f"pod_{i}") for i in range(1, 6)]  # Generate 5 forms
    if request.method == "POST":
        if all(form.validate_on_submit() for form in forms):
            report_date = datetime.now().strftime("%Y-%m-%d")
            report_time = datetime.now().strftime("%H:%M:%S")
            
            # Collect form data
            email_body = f"Daily SAC Report - {report_date} {report_time}\n\n"
            for i, form in enumerate(forms, start=1):
                email_body += f"--- POD {i} ---\n"
                email_body += f"Site Location: {form.site_location.data}\n"
                email_body += f"POD ID: {form.pod_id.data}\n"
                email_body += f"POD Number: {form.pod_number.data}\n"
                email_body += f"Pod Usage: {form.pod_usage.data}\n"
                email_body += f"Generator Status: {form.generator_status.data}\n"
                email_body += f"Cleaned Toilets Male: {form.cleaned_male.data}\n"
                email_body += f"Cleaned Toilets Female: {form.cleaned_female.data}\n"
                email_body += f"Diesel Gauge: {form.diesel_gauge.data}%\n"
                email_body += f"Oil Gauge: {form.oil_gauge.data}%\n"
                email_body += f"Used as Storage: {form.storage.data}\n"
                email_body += f"Comments: {form.comments.data}\n\n"
            
            # Send email
            send_email("zzubiks@gmail.com", "Daily SAC Report", email_body)
            flash("Report sent successfully!", "success")
            return redirect(url_for("index"))
        else:
            flash("Please fill out all required fields.", "danger")

    return render_template("index.html", forms=forms)


def send_email(to_email, subject, body):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "your_email@gmail.com"  # Replace with your email
        sender_password = "your_password"  # Replace with your email password

        # Set up email content
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = to_email

        # Send email via SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    app.run(debug=True)
