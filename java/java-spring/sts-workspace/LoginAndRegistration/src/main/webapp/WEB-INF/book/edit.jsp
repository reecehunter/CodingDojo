<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %>  
  
<!DOCTYPE html>
<html>
<head>
	<meta charset="ISO-8859-1">
	<title>Edit Book</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
	<div class="d-flex justify-content-between">
		<div>
			<h1>Change Your Entry</h1>
		</div>
		<div>
			<p><a href="/books">Back to the shelves</a></p>
		</div>
	</div>
	
	<form:form action="/books/process/edit/${book.id}" method="POST" modelAttribute="newBook" class="container">
		<form:input path="user" class="form-control" type="hidden" value="${book.user.id}"/>
		<div class="form-group">
			<form:label path="title">Title:</form:label>
			<form:errors path="title" class="d-block text-danger"/>
			<form:input path="title" class="form-control" value="${book.title}"/>
		</div>
		<div class="form-group">
			<form:label path="author">Author:</form:label>
			<form:errors path="author" class="d-block text-danger"/>
			<form:input path="author" class="form-control" value="${book.author}"/>
		</div>
		<div class="form-group">
			<form:label path="thoughts">My Thoughts:</form:label>
			<form:errors path="thoughts" class="d-block text-danger"/>
			<form:input path="thoughts" class="form-control" value="${book.thoughts}"/>
		</div>
		<input type="submit" value="Submit" class="btn btn-primary form-control"/>
	</form:form>
	
</body>
</html>