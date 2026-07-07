import './header.css'

function Header()
{
    return (
        <header className="header">
            <a href="/" className="site_branding" aria-label="Government of National Capital Territory of Delhi home">
                <img
                    className="site_branding_logo"
                    src="https://delhi.gov.in/sites/default/files/emblem-dark.png"
                    alt="Government emblem"
                />

                <span className="site_branding_text">
                    <span className="site_branding_english">
                        Government of National Capital Territory of Delhi
                    </span>
                    <span className="site_branding_hindi">
                        राष्ट्रीय राजधानी क्षेत्र दिल्ली सरकार
                    </span>
                </span>
            </a>
        </header>
    );
};
export default Header;
