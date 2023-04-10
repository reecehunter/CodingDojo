<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Fruit Store</title>
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
</head>
<body>
	<h1 class="mb-5">Fruit Store</h1>
	
	<table class="table">
	  <thead>
	    <tr>
	      <th scope="col">Name</th>
	      <th scope="col">Price</th>
	    </tr>
	  </thead>
	  <tbody>
	  
		<c:forEach var="fruit" items="${fruits}">
		    <tr>
		      <td><c:out value="${fruit.name}"></c:out></td>
		      <td><c:out value="${fruit.price}"></c:out></td>
		    </tr>
		</c:forEach>
	  </tbody>
	</table>
	
</body>
</html>