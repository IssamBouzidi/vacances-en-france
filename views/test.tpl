	<!DOCTYPE html>
<html lang="en">
 
<head>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
<script type="text/javascript">
  $(document).ready(function() {
    $('form').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/test2',
            data: $(this).serialize(),
            success: function(response) {
                $('#ajaxP').html(response);
            }
        });

        e.preventDefault();
    });
})
</script>
</head>
 
<body>
    <div class="container">
<form method="POST" action="/test2">
        <input id="ajaxTextbox" name="text" type"text" />
        <input id="ajaxButton" type="button" value="Submit" />
    </form>
    <p id="ajaxP">Nothing to see here.</p>
     </div>  
</body>
 
</html>