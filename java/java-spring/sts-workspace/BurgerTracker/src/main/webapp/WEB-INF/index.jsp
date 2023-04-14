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
	<h1>Burger Tracker</h1>
	<table class="table mb-5">
	  <thead>
	    <tr>
	      <th scope="col">Burger Name</th>
	      <th scope="col">Restaurant Name</th>
	      <th scope="col">Rating (out of 5)</th>
	    </tr>
	  </thead>
	  <tbody>
	  
		<c:forEach var="burger" items="${burgers}">
		    <tr>
		      <td><c:out value="${burger.name}"></c:out></td>
		      <td><c:out value="${burger.restaurantName}"></c:out></td>
		      <td><c:out value="${burger.rating}"></c:out></td>
		    </tr>
		</c:forEach>
	  </tbody>
	</table>
	
	<h1>Add a Burger:</h1>
	<p class="text-danger">Notes must not be blank</p>
	
	<form:form action="/burgers/new" method="POST" modelAttribute="burger">
		<div class="form-group">
			<form:label path="name">Burger Name:</form:label>
			<form:errors path="name"/>
			<form:input path="name" class="form-control"/>
		</div>
		
		<div class="form-group">
			<form:label path="restaurantName">Restaurant Name:</form:label>
			<form:errors path="restaurantName"/>
			<form:input path="restaurantName" class="form-control"/>
		</div>
		
		<div class="form-group">
			<form:label path="rating">Rating:</form:label>
			<form:errors path="rating"/>
			<form:input path="rating" type="number" class="form-control"/>
		</div>
		
		<div class="form-group">
			<form:label path="notes">Notes:</form:label>
			<form:errors path="notes"/>
			<form:input path="notes" class="form-control"/>
		</div>
		
		<input type="submit" value="Submit" class="btn btn-primary form-control"/>
	</form:form>
	
</body>
</html>