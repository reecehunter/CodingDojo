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
	<h1>Save Travels</h1>
	<table class="table mb-5">
	  <thead>
	    <tr>
	      <th scope="col">Expense</th>
	      <th scope="col">Vendor</th>
	      <th scope="col">Amount</th>
	      <th scope="col">Actions</th>
	    </tr>
	  </thead>
	  <tbody>
	  
		<c:forEach var="expense" items="${expenses}">
		    <tr>
		      <td><a href="/expenses/${expense.id}"><c:out value="${expense.name}"></c:out></a></td>
		      <td><c:out value="${expense.vendor}"></c:out></td>
		      <td><c:out value="${expense.amount}"></c:out></td>
		      <td>
		      	<a href="/expenses/edit/${expense.id}">Edit</a>
		      	<form action="/expenses/delete/${expense.id}" method="post">
					<input type="hidden" name="_method" value="delete">
		      		<input type="submit" value="Delete" class="btn btn-danger"/>
		      	</form>
		      </td>
		    </tr>
		</c:forEach>
	  </tbody>
	</table>
	
	<h1>Add an Expense:</h1>
	<p class="text-danger">Description must not be blank</p>
	
	<form:form action="/expenses/new" method="POST" modelAttribute="expense">
		<div class="form-group">
			<form:label path="name">Expense Name:</form:label>
			<form:errors path="name"/>
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