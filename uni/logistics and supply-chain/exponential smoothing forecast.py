"""
Square brackets show the subscript of function

F[t+1] = F[t] + alpha(A[t]-1 - F[t-1])

or

F[t+1] = alpha*A[t] + (1 - alpha) * F[t]

A[t] : actual demand
F[t] : Forecast demand


"""

def exp_smooth_forecast(demands, alpha):
    forecast = [demands[0]]

    for i in range(len(demands)):
        forecast.append(alpha * demands[i] + (1 - alpha) * forecast[i])

    print(forecast)
    return f"Forecast demand: {(forecast[-1])}"



print(exp_smooth_forecast([310, 365, 395, 415, 450, 465], 0.4))
print(exp_smooth_forecast([3094, 3170, 3520, 3716, 3249, 3120], 0.2))





