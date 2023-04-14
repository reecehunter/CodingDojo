<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %>    
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Show Dojo</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>

	<h1><c:out value="${dojo.name}"/> Location Ninjas</h1>
	
	<table class="table">
	  <thead>
	    <tr>
	      <th scope="col">First Name</th>
	      <th scope="col">Last Name</th>
	      <th scope="col">Age</th>
	    </tr>
	  </thead>
	  <tbody>
	  
		<c:forEach var="ninja" items="${dojo.ninjas}">
		    <tr>
		      <td><c:out value="${ninja.firstName}"/></td>
		      <td><c:out value="${ninja.lastName}"/></td>
		      <td><c:out value="${ninja.age}"/></td>
		    </tr>
		</c:forEach>
	  </tbody>
	</table>
	
</body>
</html>