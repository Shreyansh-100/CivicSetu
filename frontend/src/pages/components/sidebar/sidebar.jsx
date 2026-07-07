import './sidebar.css'

function Sidebar()
{
    return(
 
                <nav className="side_bar">

                    <h2 className="sidebar_title">
                        Navigation
                    </h2>

                    <button className="nav_btn">
                        Main Menu
                    </button>

                    <button className="nav_btn">
                        Track Status
                    </button>

                    <button className="nav_btn">
                        Help
                    </button>

                    <button className="nav_btn">
                        Connect
                    </button>

                </nav>
               
    );
};
export default Sidebar;