<?php
  // If character is (, go up one floor
  // If character is ), go down one floor
  // Return the first time Santa is in the basement
  $input = file_get_contents("in.txt");
  $floor = 0;
  $position = 0;  
  for($i = 0; $i < strlen($input); $i++) {
    $position++;
    if($input[$i] == '(') {
      $floor++;
    } else {
      $floor--;
    }
    if($floor == -1) {
      break;
    }
  }
  echo "p2: $position\n";
?>