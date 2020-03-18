import React from 'react';
import { Provider } from 'react-redux';
import { store } from './Store';
//import { PersistGate } from 'redux-persist/integration/react';
import EditForecast from './Components/EditForecast/index'

function App() {
    return (
        <Provider store={store}>
            <EditForecast />
        </Provider>
    );
}

export default App;
