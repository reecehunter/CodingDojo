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
	<h1><c:out value="${name}"></c:out></h1>
	<p><c:out value="${itemName}"></c:out></p>
	<p><c:out value="${price}"></c:out></p>
	<p><c:out value="${description}"></c:out></p>
	<p><c:out value="${vendor}"></c:out></p>
</body>
</html>