import './footer.css'

function Footer()
{
    return(
        <footer className="footer">
    <div className="footer_left">
        <h3>Department Address</h3>
        <p>
            9th Level, 'B'-Wing, Delhi Secretariat,<br />
            I.P. Estate, New Delhi - 110002
        </p>
    </div>

    <div className="footer_right">
        <h3>Key Contact Information</h3>
        <p>Main Phone: 011-23392254, 011-23392693</p>
        <p>Email: webupdate@nic.in</p>
        <a href='https://it.delhi.gov.in/' className='link'>Department of Information Technology</a>
        
    </div>
</footer>
    );

};
export default Footer;