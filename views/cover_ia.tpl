<!doctype html>
<html lang="en">
  <head>
    % include('head.tpl', title='Head')
  </head>
  <body>
  
<div class="container-fluid">
    <form action="/cover" method="get">
        <div class="row">
            
            % include('nav.tpl', title='Navigation')

            <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-md-4">
            <h2>Analyse des pochettes d'album</h2>
            
            <div class="table-responsive">
                <table class="table table-striped table-sm">
                <thead>
                    <tr>
                    <th style="width:auto">Album</th>
                    <th style="width:30px"></th>
                    <th style="width:auto"></th>
                    <th style="width:100%"></th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <td>
                        <select name="album_cover" id="selector">
                            % for album in albums:
                                <option value="{{album[1]}}" {{!'selected="selected"' if album[2] == 1 else ""}}>{{album[0]}}</option>
                            % end
                        </select>
                    </td>
                    <td>
                        <button type="submit" style="background:transparent; border: none" title="lancer la recherche">
                        <span data-feather="search"></span>
                        </button>
                    </td>
                    </tr>
                    <tr>
                    <td>
                        <img id="originalcover" src="" style="max-height:500px"/>
                    </td>
                    <td/>
                    <td>
                        <img id="transformedcover" src="/path/to/cover" style="max-height:500px"/>
                    </td>
                    <td>
                        <ul id="transformedinfo">
                        % for identification in identifications:
                            <li><b>{{identification[0]}}</b> - {{identification[1]}}%</li>
                        % end
                        </ul>
                    </td>
                    </tr>
                </tbody>
                </table>
            </div>
            </main>
        </div>
    </form>
</div>
% include('scripts.tpl', title='Scripts')

<script type="text/javascript">

    setCover();
    if(window.location.href.endsWith("cover"))
        {
            hideTransform();
        }

    $( "#selector" ).change(function() {
        setCover();
        hideTransform();
    });

    function setCover()
    {
       var coverpath = $('#selector').val();
        $('#originalcover').attr('src',coverpath);
    }

    function hideTransform()
    {
        $('#transformedcover').hide();
        $('#transformedinfo').hide();
    }
</script>
</body>
</html>