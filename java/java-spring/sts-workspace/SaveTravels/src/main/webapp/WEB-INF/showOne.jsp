<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %>    
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Save Travels</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
	<div class="d-flex justify-content-between align-center">
		<h1>Edit Expense</h1>
		<a href="/expenses">Go back</a>
	</div>
	
	<p>Expense Name: <c:out value="${expense.name}"/></p>
	<p>Amount Spent: $<c:out value="${expense.amount}"/></p>
	<p>Vendor: <c:out value="${expense.vendor}"/></p>
	<p>Description: <c:out value="${expense.description}"/></p>
	
</body>
</html>