import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import API from '../api';

function Login() {
  const [form, setForm] = useState({
    user_id: '',
    location: '',
    login_count: '',
    previous_failures: ''
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    try {
      const response = await API.post('/predict', {
        ...form,
        login_count: parseInt(form.login_count),
        previous_failures: parseInt(form.previous_failures)
      });

      const risk = response.data.risk_score;
      alert(`Risk Score: ${risk}`);

      await API.post('/log_access', {
        user_id: form.user_id,
        risk_score: risk
      });

      navigate('/dashboard');
    } catch (err) {
      alert('Something went wrong. Check Flask backend.');
      console.error(err);
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Login Simulation</h2>
      <input name="user_id" placeholder="User ID" onChange={handleChange} /><br />
      <input name="location" placeholder="Location" onChange={handleChange} /><br />
      <input name="login_count" type="number" placeholder="Login Count" onChange={handleChange} /><br />
      <input name="previous_failures" type="number" placeholder="Previous Failures" onChange={handleChange} /><br />
      <button onClick={handleSubmit}>Predict & Log</button>
    </div>
  );
}

export default Login;
