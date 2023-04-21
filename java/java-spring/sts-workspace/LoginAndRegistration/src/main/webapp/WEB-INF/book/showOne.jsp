<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>One Book</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body class="container">
	<div class="d-flex justify-content-between align-items-center my-5">
		<h1><c:out value="${book.title}"/></h1>
		<p><a href="/books">Back to the shelves</a></p>
	</div>
	
	<h3><c:out value="${book.user.name}"/> read <c:out value="${book.title}"/> by <c:out value="${book.author}"/></h3>
	<p>Here are <c:out value="${book.user.name}"/>'s thoughts:</p>
	
	<hr class="my-5"/>
	<p><c:out value="${book.thoughts}"/></p>
	<hr class="my-5"/>

	<div class="d-flex mt-5">
		<a href="/books/edit/${book.id}">
			<button class="btn btn-primary">Edit</button>
		</a>
      	<form action="/books/delete/${book.id}" method="post">
			<input type="hidden" name="_method" value="delete"/>
      		<input type="submit" value="Delete" class="btn btn-danger"/>
      	</form>
	</div>
</body>
</html>