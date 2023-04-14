<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %>    
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
	<div class="d-flex justify-content-between align-center">
		<h1>Edit Expense</h1>
		<a href="/expenses">Go back</a>
	</div>
	
	<form:form action="/expenses/${expense.id}" method="POST" modelAttribute="expense">
		<div class="form-group">
			<form:label path="name">Expense Name:</form:label>
			<form:errors path="name"></form:errors>
			<form:input path="name" class="form-control"/>
		</div>
		
		<div class="form-group">
			<form:label path="vendor">Vendor:</form:label>
			<form:errors path="vendor"/>
			<form:input path="vendor" class="form-control"/>
		</div>
		
		<div class="form-group">
			<form:label path="amount">Amount:</form:label>
			<form:errors path="amount"/>
			<form:input path="amount" type="number" class="form-control"/>
		</div>
		
		<div class="form-group">
			<form:label path="description">Description:</form:label>
			<form:errors path="description"/>
			<form:input path="description" class="form-control"/>
		</div>
		
		<input type="submit" value="Submit" class="btn btn-primary form-control"/>
	</form:form>
</body>
</html>