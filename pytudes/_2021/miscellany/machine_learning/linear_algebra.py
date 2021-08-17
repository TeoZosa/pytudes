import numpy as np
import scipy.spatial


def cosine_similarity(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """For samples x features matrixes or 1 x features column vectors

    [
        [cosine_similarity(A[0], B[0]),              ... ,cosine_similarity(A[0], B[len(B)-1])],
        ...,
        [cosine_similarity(A[len(A)-1], B[len(B]-1), ... ,cosine_similarity(A[len(A)-1], B[len(B)-1])],
    ]

    [
        [A_1 . B_1, ... ,A_1 . B_m],
        ...
        [A_n . B_1, ... ,A_n . B_m],
    ]
    Args:
        A:
        B:

    Examples:
        >>> x = np.array([3, 45, 7, 2] )
        >>> y = np.array([2,54,13,15] )
        >>> cosine_similarity(x, y)[0]
        0.9722842517123499
        >>> assert cosine_similarity(x, y) == cosine_similarity(y, x)
        >>> cosine_similarity(x, x)[0]
        1.0
        >>> cosine_similarity(x, -x)[0]
        -1.0
        >>> cosine_similarity(x, np.zeros(x.shape))[0]
        0.0
        >>> np.testing.assert_almost_equal(cosine_similarity(x, y), 1 - scipy.spatial.distance.cosine(x, y))
        >>> a, b = np.array([x,y]), np.array([y,x])
        >>> cosine_similarity(a, a)
        array([[1.        , 0.97228425],
               [0.97228425, 1.        ]])
        >>> cosine_similarity(a, b)
        array([[0.97228425, 1.        ],
               [1.        , 0.97228425]])
        >>> np.testing.assert_almost_equal(cosine_similarity(a, b), 1 - scipy.spatial.distance.cdist(a, b, "cosine"))


    """

    # Dot product w/ normalized magnitudes
    # Note:
    #   For *vectors* A,B:
    #   - euclidean_length(B).T == euclidean_length(B)
    #   For *matrices* A,B:
    #   - length vectors multiplication broadcasting will produce a len(A) x len(B)
    #     lengths matrix s.t.
    #     `lengths[i,j] == euclidean_length(A[i]) * euclidean_length(B[j])`
    #     <=> multiplied length magnitudes corresponding to the element (A @ B.T)[i,j]

    #     lengths matrix corresponding to the multiplied lengths of corresponding column
    #     vector dot product elements in A @ B.T
    similarity = A @ B.T / (euclidean_length(A) * euclidean_length(B).T)
    return np.nan_to_num(similarity)  # Map NaN to 0


def euclidean_length(arr: np.ndarray) -> np.ndarray:
    """

    Args:
        arr:

    Examples:
        >>> x = np.array([3, 45, 7, 2] )
        >>> y = np.array([2,54,13,15] )
        >>> euclidean_length(x)[0]
        45.68369512200168
        >>> euclidean_length(y)[0]
        57.56735185849702
        >>> euclidean_length(np.array([x,y]))
        array([[45.68369512],
               [57.56735186]])

    """
    return np.linalg.norm(arr, keepdims=True, axis=len(arr.shape) - 1)
