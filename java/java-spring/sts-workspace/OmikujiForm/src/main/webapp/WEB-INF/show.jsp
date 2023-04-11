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
	<h1>Here's Your Omikuji</h1>
	
	<p>In <c:out value="${amount}"/>
	years, you will live in <c:out value="${cityName}"/>
	with <c:out value="${personName}"/>
	as your roommate, <c:out value="${hobby}"/>
	for a living. The next time you see a <c:out value="${livingThing}"/>,
	you will have good luck. Also, <c:out value="${nice}"/>.
	</p>
	
	<a href="/">Go Back</a>
</body>
</html>