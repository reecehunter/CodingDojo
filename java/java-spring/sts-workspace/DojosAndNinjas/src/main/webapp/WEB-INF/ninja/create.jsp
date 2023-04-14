<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %>    
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>New Ninja</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
	<h1>New Ninja:</h1>
	
	<form:form action="/ninjas/new" method="POST" modelAttribute="ninja" class="container">
		<div class="form-group">
			<form:label path="dojo">Dojo:</form:label>
			<form:errors path="dojo" class="d-block text-danger"/>
			<form:select path="dojo" class="form-control">
				<c:forEach var="dojo" items="${dojos}">
					<form:option value="${dojo.id}">
						<c:out value="${dojo.name}"/>
					</form:option>
				</c:forEach>
			</form:select>
		</div>
		<div class="form-group">
			<form:label path="firstName">First Name:</form:label>
			<form:errors path="firstName" class="d-block text-danger"/>
			<form:input path="firstName" class="form-control"/>
		</div>
		<div class="form-group">
			<form:label path="lastName">Last Name:</form:label>
			<form:errors path="lastName" class="d-block text-danger"/>
			<form:input path="lastName" class="form-control"/>
		</div>
		<div class="form-group">
			<form:label path="age">Age:</form:label>
			<form:errors path="age" class="d-block text-danger"/>
			<form:input path="age" class="form-control" type="number" min="1"/>
		</div>
		<input type="submit" value="Create" class="btn btn-primary form-control"/>
	</form:form>
	
</body>
</html>