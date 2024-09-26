<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

<title>Insert title here</title>
</head>
<body>

<div class="containar">

<table class="table table-bordered">
	<tr>
		<th>タイトル</th>
		<th>内容</th>
		<th>スタッフ・キャスト</th>
	</tr>
	<c:forEach items="${movieList}" var="dto">
		<tr>
			<td><c:out values="${dto.title}"></td>
			<td><c:out values="${dto.txt}"></td>
			<td><c:out values="${dto.cast}"></td>
		</tr>
	</c:forEach>
</table>

</div>

</body>
</html>