<!doctype html>
<html lang="en">
  <head>
    % include('head.tpl', title='Head')
  </head>
  <body>
  % include('top_nav.tpl', title='Top navigation')

<div class="container-fluid">
  <div class="row">
    
	% include('nav.tpl', title='Navigation')

    <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-md-4">
      <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">

    <form action="/load_data" method="GET">
    <div class="form-group">
    <div class="alert alert-primary" role="alert">
      {{data}}
    </div>
     <button type="submit" name="save" class="btn btn-dark">Load and Save in Database</button>
      
    </div>
      
    </form>  
      </div>
    </main>
  </div>
</div>
% include('scripts.tpl', title='Scripts')
		</body>
</html>
