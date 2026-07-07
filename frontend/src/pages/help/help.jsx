import Sidebar from "../components/sidebar/sidebar";
import "./help.css";
import Header from '../components/header/header'
import Footer from '../components/footer/footer'
function Help() {
    return (
        <div className="help_page">
            <Header/>

            <div className="help_body">
                <Sidebar />

                <main className="help_content">
                    <div className="help_intro">
                        <h1>Citizen Help and Support</h1>

                        <p>
                            Please refer to the frequently asked questions below for
                            guidance on registering civic grievances, tracking complaint
                            status, and accessing citizen support services.
                        </p>
                    </div>

                    <section className="faq_section">
                        <h2>Frequently Asked Questions</h2>

                        <details className="faq_item">
                            <summary>How do I lodge a complaint?</summary>
                            <p>
                                Navigate to the Lodge Complaint page and provide the
                                required details, including the issue category,
                                description, location, and supporting documents. After
                                submission, you will receive a unique Complaint ID.
                            </p>
                        </details>

                        <details className="faq_item">
                            <summary>How can I track my registered complaint?</summary>
                            <p>
                                Visit the Track Complaint page and enter your Complaint ID.
                                The portal will display the current status, recent updates,
                                and the department responsible for the complaint.
                            </p>
                        </details>

                        <details className="faq_item">
                            <summary>
                                What details are required while lodging a complaint?
                            </summary>
                            <p>
                                Provide the issue category, a clear description, the
                                incident location, and any relevant photographs or
                                supporting documents. Complete information helps the
                                concerned department process the complaint efficiently.
                            </p>
                        </details>

                        <details className="faq_item">
                            <summary>
                                When can I expect a response after submitting my complaint?
                            </summary>
                            <p>
                                Response times vary according to the nature, severity, and
                                complexity of the issue. You can monitor progress and
                                department updates through the Track Complaint page.
                            </p>
                        </details>

                        <details className="faq_item">
                            <summary>How can I report an urgent issue?</summary>
                            <p>
                                Use the official contact details shown on the Connect page
                                to notify the appropriate authority. For emergencies,
                                contact the relevant emergency service directly.
                            </p>
                        </details>

                        <details className="faq_item">
                            <summary>
                                Will I need to visit the concerned department?
                            </summary>
                            <p>
                                Most complaints are processed digitally. If additional
                                verification or clarification is required, the concerned
                                authority may contact you with further instructions.
                            </p>
                        </details>

                        <details className="faq_item">
                            <summary>
                                How can I contact the concerned authority directly?
                            </summary>
                            <p>
                                Visit the Connect page for official helpline numbers, email
                                addresses, office information, and other approved contact
                                channels.
                            </p>
                        </details>
                    </section>
                </main>
            </div>
           <Footer/>
        </div>
    );
}

export default Help;
