import './Auth.css'
function Auth()
{
    return (
        <div className="auth-page">
            <div className="auth-card">
                <div className='left-panel'>
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
    );
}
export default Auth;