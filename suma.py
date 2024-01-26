@app.route("/suma/num1/num2")
 def suma(num1,num2)
 result=(num1 + num2)
 return F"Primer{num1} segundo{num2}el resultado es
 {result}"