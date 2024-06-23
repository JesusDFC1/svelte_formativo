<script>
    import { navigate } from 'svelte-routing';

    let correo = '';
    let clave = '';
    let mensaje = '';

    async function handleLogin(event) {
        event.preventDefault(); // Prevenir el comportamiento por defecto del formulario

        try {
            const response = await fetch('http://localhost:5000/registro_cliente/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ correo, clave })
            });

            const data = await response.json();
            mensaje = data.mensaje;

            if (response.ok) {
                navigate('/menu'); 
            } else {
               
                console.error('Error:', mensaje);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    }
</script>

<main>
    <div class="login-container">
        <form class="login-form" on:submit={handleLogin}>
            <h2>Login</h2>
            <div class="form-control">
                <label for="correo">Correo Electrónico:</label>
                <input type="email" id="correo" placeholder="Correo" bind:value={correo} required>
            </div>
            <div class="form-control">
                <label for="clave">Clave:</label>
                <input type="password" id="clave" placeholder="Clave" bind:value={clave} required>
            </div>
            <button type="submit" class="login-button">Ingresar</button>
            {#if mensaje}
                <p>{mensaje}</p>
            {/if}
        </form>
    </div>
</main>

<style>
    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .login-form {
        background-color: #f3f3f3;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .form-control {
        margin-bottom: 1rem;
    }

    .login-button {
        background-color: #007BFF;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 4px;
        cursor: pointer;
    }

    .login-button:hover {
        background-color: #0056b3;
    }



.login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f0f0f0;
    }

    .login-form {
        background-color: #fff;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 400px;
    }

    .login-form h2 {
        margin-bottom: 1rem;
        color: #333;
    }

    .form-control {
        margin-bottom: 1rem;
    }

    .form-control label {
        display: block;
        margin-bottom: 0.5rem;
        color: #555;
    }

    .form-control input {
        width: 100%;
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 1rem;
    }

    .login-button {
        width: 100%;
        padding: 0.75rem;
        border: none;
        border-radius: 4px;
        background-color: #5928c4;
        color: #000000;
        font-size: 1rem;
        cursor: pointer;
    }

    .login-button:hover {
        background-color: #000000;
    }	
</style>
