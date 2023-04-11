<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<h1>Send an Omikuji</h1>
	<form action="/send" method="POST">
		<label for="amount">Pick any number from 1 to 25</label>
		<input type="number" name="amount" min="1" max="25">
		
		<label for="cityName">Enter the name of any city</label>
		<input type="text" name="cityName">
		
		<label for="personName">Enter the name of any real person</label>
		<input type="text" name="personName">
		
		<label for="hobby">Enter professional endeavor or hobby</label>
		<input type="text" name="hobby">
		
		<label for="livingThing">Enter any type of living thing</label>
		<input type="text" name="livingThing">
		
		<label for="nice">Say something nice to someone</label>
		<input type="text" name="nice">
		
		<input type="submit" value="Send">
	</form>
</body>
</html>