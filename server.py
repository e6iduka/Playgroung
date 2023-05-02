from flask import Flask, render_template  
app = Flask(__name__)  



@app.route('/play')
def hello_world():
    return render_template('playgroung.html')

@app.route("/play/<number_of_boxes>")
def repeat(number_of_boxes):
    repeat = int(number_of_boxes)
    return render_template('playground2.html', repeat=repeat)

@app.route("/play/<number_of_boxes>/<color_change>")
def boxcolor(number_of_boxes,color_change):
    repeat = (int(number_of_boxes))
    colorChange = color_change
    return render_template('playground3.html', repeat = repeat, colorChange = colorChange )

if __name__=="__main__":   
    app.run(debug=True) 