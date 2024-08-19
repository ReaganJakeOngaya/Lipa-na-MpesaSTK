import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import './App.css';
import Home from './pages/Home'

function App() {
  return (
    <div className="App">
      
      <div style={{padding:'20px'}}>
        <Router>
        <Routes>
          <Route path='/' element={<Home />}></Route>
        </Routes>
        </Router>
      </div>
      
    </div>
  );
}

export default App;
