<?php
if (isset($_POST['submit'])) {
    $uploadsDir = '/uploads/';
    $okFlag = 1;

		// Absolute file path of FILE where it is defined. Using this path, we can set up a ROOT FOLDER for the site.
    define('SITE_ROOT', realpath(dirname(__FILE__)));

		// Create a folder if it doesn't exist, to upload the files
    if (!file_exists(SITE_ROOT . $uploadsDir)) {
        mkdir(SITE_ROOT . $uploadsDir, 0777, true);
    }
    // Looping all files
    foreach ($_FILES['file']['name'] as $key => $error) {
        if ($error == UPLOAD_ERR_OK) {
            $targetFile = $uploadsDir . basename($_FILES['file']['name'][$key]);
            $fileType   = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));
            // Check if file type is XML
            if ($fileType != "xml") {
                echo "Only XML files allowed";
                $okFlag = 0;
                break;
            }
            // Check if file already exists
            if (file_exists(SITE_ROOT . $targetFile)) {
                echo "Sorry, file already exists.";
                $okFlag = 0;
                break;
            }
            try {
								// Upload file
                move_uploaded_file($_FILES['file']['tmp_name'][$key], SITE_ROOT . $targetFile);
            }
            catch (Exception $e) {
                $okFlag = 0;
                echo 'Message: ' . $e->getMessage();
            }
        }
    }

    if($okFlag){
      echo "Upload successful";
    }

		// Regex to check to file name - Not used currently
    function check_file_uploaded_name($filename)
    {
        (bool) ((preg_match("`^[-0-9A-Z_\.]+$`i", $filename)) ? true : false);
    }
}
?>
