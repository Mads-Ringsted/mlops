import pytest
from tests import _PATH_DATA
import torch
from src.models.model import MyAwesomeModel

@pytest.mark.parametrize("batch_size", [30, 64, 100])
def test_model(batch_size):
    trainset = torch.load(_PATH_DATA + '/processed/trainset.pt')
    testset = torch.load(_PATH_DATA + '/processed/testset.pt')

    trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True)
    images, labels = next(iter(trainloader))
    model = MyAwesomeModel()
    assert images.shape == (batch_size, 28,28) 
    assert model(images).shape == (batch_size,10), "Dataset did not output correct shape corresponding to batch size"

# tests/test_model.py
def test_error_on_wrong_shape():
   with pytest.raises(ValueError, match='Expected input to a 3D tensor'):
      model = MyAwesomeModel()
      model(torch.randn(28,28))


