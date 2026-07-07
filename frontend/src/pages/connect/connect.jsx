import './connect.css'
import Sidebar from '../components/sidebar/sidebar';
import Header from '../components/header/header';
import Footer from '../components/footer/footer'
function Connect()
{
    return(
        <div className='connect_page'>
            <Header/>
            <div className='connect_body'>
                <Sidebar/>

                <main className='connect_content'>
                    <section className='connect_details'>
                        <h1>Contact and Emergency Support</h1>
                        <p>
                            For urgent assistance or department-specific support, please use the contact details listed below. Select the relevant service to view the appropriate helpline and office information.
                        </p>
                    </section>

                    <section className='contact_details'>
                        <details className='contact_drop'>
                            <summary>General Public Helpline</summary>
                            <p>Helpline Number: XXXXXXX</p>
                            <p>Office Address: CivicSetu Head Office, XYZ</p>
                        </details>

                        <details className='contact_drop'>
                            <summary>Fire Department</summary>
                            <p>Emergency Number: XXXXXXX</p>
                            <p>Office Address: Fire Department Head Office, XYZ</p>
                        </details>

                        <details className='contact_drop'>
                            <summary>Delhi Police</summary>
                            <p>Emergency Number: XXXXXXX</p>
                            <p>Office Address: Delhi Police Headquarters, XYZ</p>
                        </details>

                        <details className='contact_drop'>
                            <summary>Medical Emergency</summary>
                            <p>Emergency Number: XXXXXXX</p>
                            <p>Office Address: Medical Emergency Control Room, XYZ</p>
                        </details>

                        <details className='contact_drop'>
                            <summary>Public Works Department</summary>
                            <p>Helpline Number: XXXXXXX</p>
                            <p>Office Address: Public Works Department Office, XYZ</p>
                        </details>

                        <details className='contact_drop'>
                            <summary>CivicSetu Support</summary>
                            <p>Helpline Number: XXXXXXX</p>
                            <p>Office Address: CivicSetu Support Centre, XYZ</p>
                        </details>
                    </section>
                </main>
            </div>
        <Footer/>
        </div>
    );
};
export default Connect;
