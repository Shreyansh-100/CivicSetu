import "./dash.css";
import Sidebar from '../components/sidebar/sidebar'
import Header from "../components/header/header";
import Footer from '../components/footer/footer'


function Dash()
{
    return (
        <div className="dash_page">

            <Header/>

            <div className="body_container">

                <Sidebar/>

                <main className="main_content">

                    

                    <p className="intro_text">
                        Welcome to the Civic Grievance Portal.
                        Citizens can report civic issues such as
                        damaged roads, drainage problems, traffic
                        signal failures and other public service
                        concerns.
                    </p>

                    <p className="caution_text">
                        Please ensure that all details entered are
                        accurate and complete. Incorrect information
                        may delay the processing and resolution of
                        your complaint.
                    </p>

                    <button className="lodge_btn">
                        Lodge Complaint
                    </button>

                    <button className="logout_btn">
                        Logout
                    </button>

                </main>

            </div>
            <Footer/>
        </div>
    );
}

export default Dash;
