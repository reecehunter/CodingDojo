<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %>  
  
<!DOCTYPE html>
<html>
<head>
	<meta charset="ISO-8859-1">
	<title>Login & Registration</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
	<h1>Welcome!</h1>
	<p>Join our growing community.</p>
	
	<form:form action="/users/process/register" method="POST" modelAttribute="newUser" class="container">
		<h2>Register</h2>
		<div class="form-group">
			<form:label path="username">Username:</form:label>
			<form:errors path="username" class="d-block text-danger"/>
			<form:input path="username" class="form-control"/>
		</div>
		<div class="form-group">
			<form:label path="email">Email:</form:label>
			<form:errors path="email" class="d-block text-danger"/>
			<form:input path="email" class="form-control"/>
		</div>
		<div class="form-group">
			<form:label path="password">Password:</form:label>
			<form:errors path="password" class="d-block text-danger"/>
			<form:input path="password" class="form-control"/>
		</div>
		<div class="form-group">
			<form:label path="confirmPassword">Confirm Password:</form:label>
			<form:errors path="confirmPassword" class="d-block text-danger"/>
			<form:input path="confirmPassword" class="form-control"/>
		</div>
		<input type="submit" value="Register" class="btn btn-primary form-control"/>
	</form:form>
	
	<hr class="my-5"/>
	
	<form:form action="/users/process/login" method="POST" modelAttribute="loginUser" class="container">
		<h2>Login</h2>
		<div class="form-group">
			<form:label path="email">Email:</form:label>
			<form:errors path="email" class="d-block text-danger"/>
			<form:input path="email" class="form-control"/>
		</div>
		<div class="form-group">
			<form:label path="password">Password:</form:label>
			<form:errors path="password" class="d-block text-danger"/>
			<form:input path="password" class="form-control"/>
		</div>
		<input type="submit" value="Login" class="btn btn-primary form-control"/>
	</form:form>
	
</body>
</html>