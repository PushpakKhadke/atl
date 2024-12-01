<?php
include 'db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = password_hash($_POST['password'], PASSWORD_BCRYPT);

    // Insert user into database
    $sql = "INSERT INTO users (username, password) VALUES ('$username', '$password')";
    if ($conn->query($sql) === TRUE) {
        echo "Registration successful! <a href='login.php'>Login Here</a>";
    } else {
        echo "Error: " . $conn->error;
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
<h1>Register</h1>
<form method="POST">
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username" required><br><br>
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password" required><br><br>
    <button type="submit">Register</button>
</form>
</body>
</html>
