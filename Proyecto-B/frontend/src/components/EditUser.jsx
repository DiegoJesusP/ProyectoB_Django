import { useState, useEffect } from 'react';
import axios from 'axios';

function EditUser({ userEdit, onSave, handleClose }) {
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [control_number, setControlNumber] = useState("");
  const [age, setAge] = useState("");
  const [tel, setTel] = useState("");

  const [loading, setLoading] = useState(true);
  const sesion = localStorage.getItem('accessToken');

  useEffect(() => {
    if (userEdit) {
      setName(userEdit.name);
      setSurname(userEdit.surname);
      setControlNumber(userEdit.control_number);
      setAge(userEdit.age);
      setTel(userEdit.tel);
      setLoading(false);
    }
  }, [userEdit]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!name || !surname || !control_number || !age || !tel) {
        alert("Por favor, completa todos los campos.");
        return;
    }
    const data = { name, surname, control_number, age, tel };

    if (userEdit) {
      try {
        await axios.put(`http://127.0.0.1:8000/users/api/${userEdit.id}/`, data, {
          headers: {
            Authorization: `Bearer ${sesion}`,
          },
        });
        onSave();
      } catch (error) {
        console.error("Error al editar Usuario", error);
      }
    }
    handleClose();
  };

  if (loading) return <div>Cargando...</div>;

  return (
    <div className="modal" style={{ display: 'block' }}>
      <div className="modal-content">
        <h2>Editar Usuario</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Nombre</label>
            <input
              type="text"
              name="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="form-control"
            />
          </div>
          <div className="form-group">
            <label>Apellido</label>
            <input
              type="text"
              name="surname"
              value={surname}
              onChange={(e) => setSurname(e.target.value)}
              className="form-control"
            />
          </div>
          <div className="form-group">
            <label>Control Número</label>
            <input
              type="text"
              name="control_number"
              value={control_number}
              onChange={(e) => setControlNumber(e.target.value)}
              className="form-control"
            />
          </div>
          <div className="form-group">
            <label>Edad</label>
            <input
              type="number"
              name="age"
              value={age}
              onChange={(e) => setAge(e.target.value)}
              className="form-control"
            />
          </div>
          <div className="form-group">
            <label>Teléfono</label>
            <input
              type="text"
              name="tel"
              value={tel}
              onChange={(e) => setTel(e.target.value)}
              className="form-control"
            />
          </div>
          <div className="modal-footer">
            <button
              type="button"
              className="btn btn-secondary"
              onClick={handleClose}
            >
              Cancelar
            </button>
            <button type="submit" className="btn btn-primary">
              Guardar cambios
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default EditUser;
