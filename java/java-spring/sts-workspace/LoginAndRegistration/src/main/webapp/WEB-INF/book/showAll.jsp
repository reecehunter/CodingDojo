<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>All Books</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body class="my-5 mx-5">
	<div class="d-flex justify-content-between">
		<div>
			<h1>Welcome, <c:out value="${user.username}"/>!</h1>
			<p>Books from everyone's shelves</p>
		</div>
		<div>
			<p><a href="/users/logout">Log Out</a></p>
			<p><a href="/books/new">+ Add a book to my shelf</a></p>
		</div>
	</div>
	
	<table class="table">
	    <thead>
	        <tr>
	            <th>ID</th>
	            <th>Title</th>
	            <th>Author Name</th>
	            <th>Posted By</th>
	        </tr>
	    </thead>
    	<tbody>
			<c:forEach var="book" items="${books}">
				<tr>
			         <td><c:out value="${book.id}"/></td>
			         <td><a href="/books/${book.id}"><c:out value="${book.title}"/></a></td>
			         <td><c:out value="${book.author}"/></td>
			         <td><c:out value="${book.user.username}"/></td>
			    </tr>
			</c:forEach>
    	</tbody>
	</table>
</body>
</html>