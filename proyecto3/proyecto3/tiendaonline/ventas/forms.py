
{% extends "base.html" %}

{% block title %}Landing Page{% endblock %}

{% block header %} <h1>Nuestro Producto Estrella</h1>
<h2>Regí strate dentro de los 100 primeros y recibirá s un
descuento</h2>
{% endblock %}
{% block imagen %} <img
src="https://www.cfg.com/images/cfg1a_new.gif"
height="250px"> <p>Image copyrights to
https://www.cfg.com/</p>{% endblock %}{% block formulario %}
<form> <p>Nombre</p> <input type="text">
<p>Email</p> <input type="email"/> <br> <br>
<button type="submit">Regí strate</button> </form> <br>
<h3>¡Nuestros Beneficios!</h3> <ul> <li>Rapidez</li>
<li>Seguridad</li> <li>Gran Precio</li>
<li>Flexibilidad</li> </ul>{% endblock %}{% block footer %}
<br> <p> <a href="">Like Red Social 1</a> | <a
href="">Like Red Social 2</a> | <a href="">Like Red Social
3</a> | <a href="">Like Red Social 4</a> </p> <br>
<p>Copyright &copy; 2019-2020 - Desarrollos de Landing Pages
Inc.</p>{% endblock %}