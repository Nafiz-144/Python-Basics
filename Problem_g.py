import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, ifft


def generate_noi_spe(clean_speech, noise_std):

    noise = np.random.normal(0, noise_std, size=len(clean_speech))
    return clean_speech + noise


def basis_expa(x):

    return fft(x)


def least_squares_regres(y, Phi):

    return np.linalg.pinv(Phi) @ y


def filter_and_reconstruct(y_hat, Phi):

    return np.real(ifft(y_hat))


def reduce_noise(clean_speech, noise_std):

    noisy_speech = generate_noi_spe(clean_speech, noise_std)
    Phi = basis_expa(noisy_speech)
    y_hat = least_squares_regres(noisy_speech, Phi)
    denoised_speech = filter_and_reconstruct(y_hat, Phi)
    return denoised_speech


clean_speech = np.sin(2*np.pi*1000*np.linspace(0, 1, 1000))


noise_std = 0.1


noisy_speech = generate_noi_spe(clean_speech, noise_std)


denoised_speech = reduce_noise(clean_speech, noise_std)


plt.plot(clean_speech, label='Clean Speech')
plt.plot(noisy_speech, label='Noisy Speech')
plt.plot(denoised_speech, label='Denoised Speech')
plt.legend()
plt.show()
