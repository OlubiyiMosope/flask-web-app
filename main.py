from flask import Flask, render_template
app = Flask(__name__)

nums = range(1,10001)
thirds = nums[::3]
tens = nums[::10]



#@app.context_processor
def check_prime(num):
    test_prime = []
    
    for n in range(1,num):
        if num % n == 0:
            test_prime.append(n)

    if len(test_prime) == 1:
        return True
        del test_prime
    return False
    
#app.jinja_env.globals.update(check_prime=check_prime) 
    

@app.route("/")
def home():
    return render_template('index.html', nums=nums, thirds=thirds, tens=tens, check_prime=check_prime)


if __name__ == '__main__':
    app.run(debug=True)
