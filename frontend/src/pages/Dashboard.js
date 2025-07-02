import React, { useEffect, useState } from 'react';
import API from '../api';

function Dashboard() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    API.get('/get_logs')
      .then((res) => {
        setLogs(res.data.logs);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Access Logs</h2>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>User ID</th>
            <th>Risk Score</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log, index) => (
            <tr key={index}>
              <td>{log.user_id}</td>
              <td>{log.risk_score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard;
