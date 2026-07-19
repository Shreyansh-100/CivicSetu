import './Auth.css'
import { useState } from "react";
import Header from '../components/header/header';
import Footer from '../components/footer/footer'
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Auth()
{
    const navigate=useNavigate();
    const [username,setUsername]=useState("");
    const [password,setPassword]=useState("");

    const [error,setError]=useState("");
    const[isLoading,setIsLoading]=useState(false);


    const handlelogin=async () => {
        setError("");
        setIsLoading(true);

        try
        {
            const res=await axios.post(
                "http://127.0.0.1:8000/api/login/",
                {
                    username,
                    password
                }
            );
    
            console.log(res.data);
            navigate("/dashboard")
        }
        catch (error)
        {
            setError("Invalid username or password");
        }

        finally{
            setIsLoading(false);
        }
    }
        
    const handleSubmit= async  (event)=> {
            event.preventDefault();
            await handlelogin();
        };
        
    
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
                    <form className='right-panel' onSubmit={handleSubmit}>
                        <label htmlFor='username'>Username</label>
                        <input
                            id='username'
                            placeholder='enter username'
                            value={username}
                            onChange={(event) => setUsername(event.target.value)}
                        />

                        <label htmlFor='password'>Password</label>
                        <input
                            id='password'
                            type='password'
                            placeholder='enter password'
                            value={password}
                            onChange={(event) => setPassword(event.target.value)}
                        />

                        {error && <p className='auth-error'>{error}</p>}

                        <button className='login' type='submit' disabled={isLoading}>
                            {isLoading ? 'Logging in...' : 'Login'}
                        </button>
                    </form>
                </div>
               
                  
            </div>
             
            <Footer/> 
        </div>
    );
}
export default Auth;
