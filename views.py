
from _init_ import *
from forms import *



@app.route('/', methods=['GET', 'POST'])
def home_page():
	form = classifyForm()
	feedback_form = feedbackForm()

	if request.method =='POST':
		if form.validate_on_submit():
			class_ = classify(str(form.sentence.data.lower()), RNN)
			if class_ is not None:
				if class_[0]>class_[1]:
					form.score.data = "Impolite"
					return render_template("home.html", form=form, feedback_form=feedback_form, color='#e33100')
				else:
					form.score.data = "Polite"
					return render_template("home.html", form=form, feedback_form=feedback_form, color='#0CB40C')
			else:
				form.score.data = "error"
			return render_template("home.html", form=form, feedback_form=feedback_form, color='#40b3ff')
	return render_template("home.html", form=form, feedback_form=None, color='#40b3ff')

@app.route('/test/') #/test/ will lead urls /test & /test/
def feedback():
	return render_template("test.html")
