<?php
    include_once 'connect.php';
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GPUTracker</title>
</head>

<body>
    <img src="logo.png" alt="GPUTracker" class ="center">
    <br><br>

    <p>This is the GPUTracker drop-down list.</p><br>
    <label for="gpus">Choose a GPU:</label>
    <!--<select name="gpus" id="gpus"> -->
        <?php
            $sql = "SELECT * FROM gpus;";
            $result = mysqli_query($conn, $sql);
            $resultcheck = mysqli_num_rows($result);

            if ($resultcheck > 0){
                while ($row = mysqli_fetch_assoc($result)) {
                    echo $row ['product_title'] . "<br>";
                }
            }
          ?>

        <!--<option value="gpu1">GPU 1</option>
          <option value="gpu2">GPU 2</option>
          <option value="gpu3">GPU 3</option>
          <option value="gpu4">GPU 4</option>
        </select> -->
        <br><br>
        </form>


</body>

</html>