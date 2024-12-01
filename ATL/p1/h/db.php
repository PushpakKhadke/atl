<?php
$conn = new mysqli("localhost", "root", "", "simple_app");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
