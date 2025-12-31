import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

# 1. Definimos las Matrices de Pauli (El ADN de SU(2))
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)

# 2. Configuración del Camino (Un círculo en el espacio)
phi_path = np.linspace(0, 2*np.pi, 200)
R = 1.0
x_path = R * np.cos(phi_path)
y_path = R * np.sin(phi_path)

# 3. El Mecanismo: La Conexión de Calibre A_mu
# Simulamos una conexión que depende de dos defectos internos.
# A_mu = A1 * s1 + A2 * s2 (Campo de gauge no-abeliano)
def get_gauge_connection(phi):
    # La intensidad del campo de gauge varía a lo largo del camino
    # representando la influencia de los dos defectos nemáticos.
    A_x = np.sin(phi) * s1 
    A_y = np.cos(phi) * s2
    return A_x, A_y

# 4. Integración del Bucle de Wilson (Transporte de Holonomía)
# U = P * exp( i * integral(A_mu dx^mu) )
U = np.eye(2, dtype=complex)
dt = phi_path[1] - phi_path[0]

for i in range(len(phi_path)-1):
    phi = phi_path[i]
    Ax, Ay = get_gauge_connection(phi)
    
    # dx y dy para el camino circular
    dx = -R * np.sin(phi) * dt
    dy = R * np.cos(phi) * dt
    
    # Exponencial ordenada (Mecanismo de Yang-Mills)
    U = expm(1j * (Ax * dx + Ay * dy)) @ U

print("--- SIMULACIÓN 24c: EL MECANISMO DE LA FUERZA DÉBIL ---")
print("\n1. Matriz de Holonomía Final (Bucle de Wilson):")
print(np.round(U, 3))

# 5. Verificación de la "Carga Débil"
# Si la matriz no es la identidad, hay una fuerza neta.
trace = np.real(np.trace(U))
print(f"\n2. Traza de la Holonomía: {trace:.3f}")

if not np.allclose(U, np.eye(2)):
    print("\nÉXITO: El mecanismo de transporte genera una curvatura de gauge.")
    print("La partícula ha 'sentido' la Fuerza Débil a través del transporte local.")