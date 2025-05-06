import React, { useEffect, useState } from 'react';
import { View, Text, FlatList } from 'react-native';
import api from '../services/api';

export default function Dashboard() {
  const [requests, setRequests] = useState([]);

  useEffect(() => {
    fetchRequests();
  }, []);

  const fetchRequests = async () => {
    const response = await api.get('/api/nurse/requests');
    setRequests(response.data);
  };

  return (
    <View>
      <Text>Pending Requests</Text>
      <FlatList
        data={requests}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <Text>{item.patientId}: {item.content}</Text>
        )}
      />
    </View>
  );
}