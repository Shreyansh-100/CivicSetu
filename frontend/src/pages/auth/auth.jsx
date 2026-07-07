import './Auth.css'
import Header from '../components/header/header';
import Footer from '../components/footer/footer'
function Auth()
{
    return (
        <div> 
            <Header/>
            <div className="auth-page">
            
                <div className="auth-card">
                    <div className='left-panel'>
                        <img
                            src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Emblem_of_India_%28Government_Gazette%29.svg"
                            alt="Delhi Government Logo"
                            className="govt-logo"
                            />
                        <h1 className='head'>CivicSetu</h1>
                        <p className='desc'>
                            
                            Report.Track.Resolve
                        </p>
                    </div>
                    <div className='right-panel'>
                        <label htmlFor='username'>Username</label>
                        <input id='username' placeholder='enter username' />

                        <label htmlFor='password'>Password</label>
                        <input id='password' type='password' placeholder='enter password'/>

                        <button className='login'>Login</button>
                    </div>
                </div>
               
                  
            </div>
             
            <Footer/> 
        </div>
    );
}
export default Auth;