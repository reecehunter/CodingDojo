<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Ninja Gold Game</title>
<link href="/css/styles.css" rel="stylesheet" type="text/css">
</head>
<body>
	<p>Your Gold: <c:out value="${gold}"/></p>
	
	<div class="container">
		<form action="/findGold" method="POST" class="card">
			<h3>Farm</h3>
			<p>(Earns 10-20 gold)</p>
			<input type="hidden" name="location" value="farm">
			<input type="submit" value="Find Gold">
		</form>
		<form action="/findGold" method="POST" class="card">
			<h3>Cave</h3>
			<p>(Earns 5-10 gold)</p>
			<input type="hidden" name="location" value="cave">
			<input type="submit" value="Find Gold">
		</form>
		<form action="/findGold" method="POST" class="card">
			<h3>House</h3>
			<p>(Earns 2-5 gold)</p>
			<input type="hidden" name="location" value="house">
			<input type="submit" value="Find Gold">
		</form>
		<form action="/findGold" method="POST" class="card">
			<h3>Quest</h3>
			<p>(Earns 0-50 gold)</p>
			<input type="hidden" name="location" value="quest">
			<input type="submit" value="Find Gold">
		</form>
	</div>
		
	<div class="card">
		<c:forEach var="activity" items="${activities}">
		<p><c:out value="${activity}"/></p>
		</c:forEach>
	</div>
</body>
</html>