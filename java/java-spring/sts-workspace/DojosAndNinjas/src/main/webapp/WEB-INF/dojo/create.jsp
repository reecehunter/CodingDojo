<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %>    
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>New Dojo</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
	<h1>New Dojo:</h1>
	
	<form:form action="/dojos/new" method="POST" modelAttribute="dojo" class="container">
		<div class="form-group">
			<form:label path="name">Name:</form:label>
			<form:errors path="name" class="d-block text-danger"/>
			<form:input path="name" class="form-control"/>
		</div>
		<input type="submit" value="Create" class="btn btn-primary form-control"/>
	</form:form>
	
</body>
</html>